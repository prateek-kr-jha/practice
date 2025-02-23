const notesRouter = require('express').Router();
const Note = require('../models/note');

notesRouter.get('/', (req, resp, next) => {
    Note.find({}).then(notes => {
        if(notes) {
            resp.json(notes);
        } else {
            resp.status(404).end();
        }
    }).catch(err => {
        next(err);
    })
});

notesRouter.get('/:id', (req, resp, next) => {
    Note.findById(req.params.id).then(note => {
        if(note) {
            resp.json(note);
        } else {
            resp.status(404).end();
        }
    }).catch(err => {
        next(err);
    })
})

notesRouter.post('/', (req, resp, next) => {
    const body = req.body;


    const note = new Note({
        content: body.content,
        important: body.important || false,
        date: new Date()
    })

    note.save().then(savedNote => {
        resp.json(savedNote);
    }).catch(err => {
        next(err);
    })
})

notesRouter.delete('/:id', (request, response, next) => {
    Note.findByIdAndDelete(request.params.id)
        .then(() => {
            response.status(204).end()
        })
        .catch(error => next(error))
})

notesRouter.put('/:id', (request, response, next) => {
    const body = request.body

    const note = {
        content: body.content,
        important: body.important,
    }

    Note.findByIdAndUpdate(request.params.id, note, { new: true })
        .then(updatedNote => {
            response.json(updatedNote)
        })
        .catch(error => next(error))
})

module.exports = notesRouter;