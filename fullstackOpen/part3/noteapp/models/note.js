const mongoose = require('mongoose');

mongoose.set('strictQuery',false)

const url = process.env.MONGODB_URI;

console.log('connecting to', url);

mongoose.connect(url)
        .then(result => {
            console.log('connected to MongoDB');
        })
        .catch(error => {
            console.log('error connecting to MongoDb:', error.message);
        })

const noteSchema = new mongoose.Schema({
  content: String,
  important: Boolean,
})

noteSchema.set('toJSON', {
    transform: (document, returnObject) => {
        returnObject.id = returnObject._id.toString();
        delete returnObject._id;
        delete returnObject.__v;
    }
})

module.exports = mongoose.model('Note', noteSchema);