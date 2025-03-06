const notesRouter = require('express').Router();
const Note = require('../models/note');
const User = require('../models/user');

notesRouter.get('/', async (req, resp, next) => {
    const notes = await Note.find({}).populate('user', { username: 1, name: 1 });
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
        resp.status(400).send({ error: 'malformed id' });
    }
})

notesRouter.post('/', async (req, resp, next) => {
    const body = req.body;

    const user = await User.findById(body.userId);

    const note = new Note({
        content: body.content,
        important: body.important || false,
        date: new Date(),
        user: user.id
    })

    const savedNote = await note.save();
    user.notes = user.notes.concat(savedNote.id);
    await user.save();
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