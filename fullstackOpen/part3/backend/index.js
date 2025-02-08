const express = require('express');
const app = express();

let notes = [
    {
      id: "1",
      content: "HTML is easy",
      important: true
    },
    {
      id: "2",
      content: "Browser can execute only JavaScript",
      important: false
    },
    {
      id: "3",
      content: "GET and POST are the most important methods of HTTP protocol",
      important: true
    }
]

app.get('/', (req, resp) => {
    resp.send('<h1>Hello world</h1>')
})

app.get('/api/notes/:id', (req, resp) => {
    const id = req.params.id;
    const note = notes.find(note => note.id == id);
    if(note) {
        resp.json(note);
    } else {
        resp.status(404);
        resp.send('no such note').end();
    }
})

app.delete('/api/notes/:id', )

const PORT = 3001;

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});