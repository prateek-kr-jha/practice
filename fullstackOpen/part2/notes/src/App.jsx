import { useState, useEffect } from 'react';
import Note from './components/Note';
import noteService from './services/notes';

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
  const [newNote, setNewNote] = useState(
    'a new note....'
  );
  const [showAll, setShowAll] = useState(false);
  const [errorMessage, setErrorMessage] = useState(null);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState(''); 

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
  console.log('render', notes.length, 'notes');

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
        console.log(resp, "------------------");
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

  const handleLoogin = (event) => {
    event.preventDefault();
    console.log('logging in with', username, password)l
  }
  return (
    <div>
      <h1>Notes</h1>
      <Notification message={errorMessage} />
      <form>
        <div>
          username
          <input
          type="text"
          value={username}
          onChange={({ target }) => setUsername(target.value)}  
          />
        </div>
        <div>
          password
          <input
          type="password"
          value={password}
          onChange={({ target }) => setPassword(target.value)}  
          />
        </div>
        <button type="submit">login</button>
      </form>
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
      <form onSubmit={addNote}>
        <input 
          value={newNote}
          onChange={handleNoteChange}
        />
        <button type='submit'>save</button>
      </form>
      <Footer />
    </div>
  )
}

export default App 