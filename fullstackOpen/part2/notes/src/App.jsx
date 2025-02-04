import { useState, useEffect } from 'react';
import axios from 'axios';
import Note from './components/Note';
import noteService from './services/notes';


const App = () => {
  const [notes, setNotes] = useState([]);
  const [newNote, setNewNote] = useState(
    'a new note....'
  );
  const [showAll, setShowAll] = useState(false);

  const hook = () => {
    console.log('effect');
    noteService
    .getAll()
    .then(resp => {
        console.log('promise fullfilled');
        setNotes(resp.data);
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
      .then(resp => {
        console.log(resp, "------------------");
        setNotes(notes.concat(resp.data));
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
    .then(response => {
      setNotes(notes.map(n => n.id === id ? response.data : n))
    })
  }
  return (
    <div>
      <h1>Notes</h1>
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
    </div>
  )
}

export default App 