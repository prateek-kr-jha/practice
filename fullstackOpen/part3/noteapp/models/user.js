const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    username: String,
    passwordHash: String,
    notes: [
        {
            type: mongoose.Schema.Types.ObjectId,
            ref: 'Note',
        }
    ]
})

userSchema.set('toJSON', {
    transform: (document, returnObject) => {
        returnObject.id = returnObject._id.toString();
        delete returnObject._id;
        delete returnObject.__v;
        // the passewordHash should not be revealed
        delete returnObject.passwordHash;
    }
})

const User = mongoose.model('User', userSchema);

module.exports = User;