import { useState, useEffect } from 'react';
import Note from './components/Note';
import noteService from './services/notes';
import loginService from './services/login';
import LoginForm from './components/LoginForm';
import Togglable from './components/Togglable';
import NoteForm from './components/NoteForm'

const Notification = ({ message }) => {
  if(message === null) {
    return null;
  }

  return (
    <div className="error">
      {message}
    </div>
  )
}

const Footer = () => {
  const footerStyle = {
    color: 'green',
    fontStyle: 'italic',
    fontSize: 16
  }

  return (
    <div style={footerStyle}>
      <br />
      <em>Note app, Department of Computer Science, University of Helsinkki 2024</em>
    </div>
  )
}


const App = () => {
  const [notes, setNotes] = useState([]);
  const [showAll, setShowAll] = useState(false);
  const [errorMessage, setErrorMessage] = useState(null);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState(''); 
  const [user, setUser] = useState(null);

  const hook = () => {
    console.log('effect');
    noteService
    .getAll()
    .then(intialNote => {
        console.log('promise fullfilled');
        setNotes(intialNote);
    })
  }

  useEffect(hook, []);

  useEffect(() => {
    const loggedUserJSON = window.localStorage.getItem('loggedNoteappUser');
    console.log(JSON.parse(loggedUserJSON), "---------")
    if(loggedUserJSON) {
      const user = JSON.parse(loggedUserJSON);
      setUser(user)
      noteService.setToken(user.token)
    }
  }, [])

  const noteToShow = showAll 
    ? notes 
    : notes.filter(note => note.important)

  const addNote = (noteObject) => {
    noteService
      .create(noteObject)
      .then(returnedNote => {
        console.log(returnedNote, "------------------");
        setNotes(notes.concat(returnedNote));
      })
  }


  const toggleImportanceOf = (id) => {
    console.log('importance of ' + id + ' needs to be toggled');
    const note = notes.find(n => n.id === id)
    const changedNote = { ...note, important: !note.important }
  
    noteService
    .update(id, changedNote)
    .then(returnedNote => {
      setNotes(notes.map(n => n.id === id ? returnedNote : n))
    })
    .catch(error => {
      setErrorMessage(
        `the note '${note.content}' was already deleted from server`
      )

      setTimeout(() => {
        setErrorMessage(null)
      }, 5000);
      setNotes(notes.filter(n => n.id != id));
    })
  }

  const handleLogin = async (event) => {
    event.preventDefault();
    console.log('logging in with', username, password);
    try {
      const user = await loginService.login({
        username, password
      })

      noteService.setToken(user.token)
      window.localStorage.setItem('loggedNoteappUser', JSON.stringify(user))
      setUser(user);
      setUsername('')
      setPassword('');
    } catch(e) {
      console.log(e)
      setErrorMessage('Wrong credentials');
      setTimeout(() => {
        setErrorMessage(null)
      }, 5000)
    }
  }

  const loginForm = () => {

    return (
      <Togglable buttonLabel='login'>
        <LoginForm 
          username={username}
          password={password}
          handleUsernameChange={({ target }) => setUsername(target.value)}
          handlePasswordChange={({ target }) => setPassword(target.value)}
          handleSubmit={handleLogin}
        />
      </Togglable>
    )

  }

  const noteForm = () => (
      <Togglable buttonLabel="New Note">
        <NoteForm
          createNote={addNote}
        />
      </Togglable>
  )
  return (
    <div>
      <h1>Notes</h1>
      <Notification message={errorMessage} />
      {user === null 
        ? loginForm() 
        : noteForm()
      }
      <h2>Notes</h2>
      <div>
        <button onClick={() => setShowAll(!showAll)}>
          show {showAll ? 'important' : 'all'}
        </button>
      </div>
      <ul>
        {noteToShow.map(note => 
          <Note 
            key={note.id} 
            note={note} 
            toggleImportance= {() => toggleImportanceOf(note.id)}
          />
        )}
      </ul>
      <Footer />
    </div>
  )
}

export default App 