const mongoose = require('mongoose');
const config = require('../utils/config'); 

mongoose.set('strictQuery', false);

const url = config.MONGODB_URI;

// console.log('connecting to', url);

mongoose
    .connect(url)
    .then((result) => {
        console.log('connected to MongoDB');
    })
    .catch((error) => {
        console.log('error connecting to MongoDb:', error.message);
    });

const noteSchema = new mongoose.Schema({
    content: {
        type: String,
        minLength: 5,
        required: true,
    },
    important: Boolean,
});

noteSchema.set('toJSON', {
    transform: (document, returnObject) => {
        returnObject.id = returnObject._id.toString();
        delete returnObject._id;
        delete returnObject.__v;
    },
});

module.exports = mongoose.model('Note', noteSchema);
