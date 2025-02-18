require('dotenv').config();
const express = require('express');
const app = express();
const cors = require('cors');
const Note = require('./models/note');

const requestLogger = (request, response, next) => {
    console.log("Method:", request.method);
    console.log("Path:  ", request.path);
    console.log("Body:  ", request.body);
    console.log("---");
    next();
}

const unknownEndpoint = (request, response) => {
    response.status(404).send({error: "unknown endpoint"});
}

const errorHandler = (error, request, response, next) => {
    console.error(error.message)
  
    if (error.name === 'CastError') {
      return response.status(400).send({ error: 'malformatted id' })
    } 
  
    next(error)
  }

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
    },
    {
        id: "4",
        content: "GET ortant methods of HTTP protocol",
        important: true
      }
]

app.use(express.json());
app.use(cors());
app.use(express.static('dist'));
app.use(requestLogger);

app.get('/', (req, resp) => {
    return resp.send(notes)
})

app.get('/api/notes', (req, res) => {
    Note.find({}).then(notes => {
        console.log(notes);
        res.status(200).send(notes);
    })
})

app.get('/api/notes/:id', (req, resp, next) => {
    const id = req.params.id;

    Note.findById(id).then(note => {
        if(note) {
            resp.json(note);
        } else {
            resp.status(404);
            resp.send('no such note').end();
        }
    })
    .catch(err => {
        next(err);
    })

})

app.delete('/api/notes/:id', (req, res) => {
    const id = req.params.id;
    notes = notes.filter(note => note.id != id);

    res.status(204).end();
})

const genereateId = () => {
    const maxId = notes.length > 0 
    ? Math.max(...notes.map(n => Number(n.id))) 
    : 0;
    return String(maxId + 1);
}

app.post("/api/notes", (req, resp) => {
    const body = req.body;

    if(!body.content) {
        return resp.status(400).json({
            error: 'content missing'
        })
    }

    const note = {
        content: body.content,
        important: Boolean(body.imoortant) || false,
        id: genereateId()
    }

    notes = notes.concat(note);
    console.log(note);
    resp.json(note);
})

app.use(unknownEndpoint);
app.use(errorHandler);
const PORT = process.env.PORT || 3001;

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});