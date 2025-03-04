const notesRouter = require('express').Router();
const Note = require('../models/note');

notesRouter.get('/', async (req, resp, next) => {
    const notes = await Note.find({});
    resp.json(notes);
});

notesRouter.get('/:id', async(req, resp, next) => {
    try {
        const note = await Note.findById(req.params.id);
        if(note) {
            resp.json(note);
        } else {
            resp.status(404).end();
        }
    } catch(e) {
        resp.status(400).send({ error: 'malformatted id' });
    }
})

notesRouter.post('/', async (req, resp, next) => {
    const body = req.body;


    const note = new Note({
        content: body.content,
        important: body.important || false,
        date: new Date()
    })

    const savedNote = await note.save();
    resp.status(201).json(savedNote);
})

notesRouter.delete('/:id', async (request, response, next) => {
    await Note.findByIdAndDelete(request.params.id);
    response.status(204).end();
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