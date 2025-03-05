const bcrypt = require('bcrypt');
const userRouter = require('express').Router();
const User = require('./../models/users');
const { response } = require('../app');

userRouter.post('/', async (req, res) => {
    const { username, name, password } = req.body;

    const saltRounds = 10;
    const passwordHash = await bcrypt.hash(password, saltRounds);

    const user = new User({
        username,
        name,
        passwordHash,
    })

    const savedUser = await user.save();

    res.status(201).json(savedUser);
})

module.exports = userRouter;