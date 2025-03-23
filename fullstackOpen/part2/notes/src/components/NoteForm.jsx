import { useState } from 'react'

const NoteForm = ({ createNote }) => {
    const [newNote, setNewNote] = useState('');

    const addNote = (event) => {
        event.preventDefault();
        console.log('button clicked', event.target);
        createNote({
            content: newNote,
            important: Math.random() < 0.5
        })
        setNewNote('')
    }
    return (
        <div>
            <h2>Create a new Note</h2>
            <form onSubmit={addNote}>
            <input 
                value={newNote}
                onChange={({ target }) => setNewNote(target.value)}
            />
            <button type='submit'>save</button>
            </form>
        </div>
    )
}

export default NoteForm