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
  const [loginVisible, setLoginVisible] = useState(false)
  const [notes, setNotes] = useState([]);
  const [newNote, setNewNote] = useState(
    'a new note....'
  );
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
    if(loggedUserJSON) {
      const user = JSON.parse(loggedUserJSON);
      setUser(user)
      noteService.setToken(user.token)
    }
  }, [])

  const noteToShow = showAll 
    ? notes 
    : notes.filter(note => note.important)

  const addNote = (event) => {
    event.preventDefault();
    console.log('button clicked', event.target);
    const noteObject = {
      content: newNote,
      important: Math.random() < 0.5
    }

    noteService
      .create(noteObject)
      .then(returnedNote => {
        console.log(returnedNote, "------------------");
        setNotes(notes.concat(returnedNote));
        setNewNote('');
      })
  }

  const handleNoteChange = (event) => {
    console.log(event.target.value);
    setNewNote(event.target.value);
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
      setUser(user);
      setUsername('')
      setPassword('');
    } catch(e) {
      setErrorMessage('Wrong credentials');
      setTimeout(() => {
        setErrorMessage(null)
      }, 5000)
    }
  }

  const loginForm = () => {
    // const hideWhenVisible = { display: loginVisible ? 'none' : '' }
    // const showWhenVisible = { display: loginVisible ? '' : 'none' }

    // return (
    //   <div>
    //     <div style={hideWhenVisible}>
    //       <button onClick={() => setLoginVisible(true)}>log in</button>
    //     </div>
    //     <div style={showWhenVisible}>
    //       <LoginForm 
    //         username={username}
    //         password={password}
    //         handleUsernameChange={({ target }) => setUsername(target.value)}
    //         handlePasswordChange={({ target }) => setPassword(target.value)}
    //         handleSubmit={handleLogin}
    //       />
    //     </div>
    //   </div>
    // )

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
          onSubmit={addNote}
          value={newNote}
          handleChange={handleNoteChange}
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