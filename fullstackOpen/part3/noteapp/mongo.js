const mongoose = require('mongoose');p

if (process.argv.length<3) {
  console.log('give password as argument')
  process.exit(1)
}

const password = encodeURIComponent(process.argv[2]);
console.log(password)
const url =
  `mongodb+srv://fullstack:${password}@cluster0.2psjv.mongodb.net/noteApp?retryWrites=true&w=majority&appName=Cluster0`

mongoose.set('strictQuery',false)

mongoose.connect(url)

const noteSchema = new mongoose.Schema({
  content: String,
  important: Boolean,
})

const Note = mongoose.model('Note', noteSchema)

// const note = new Note({
//   content: 'Mongose makes thing easy',
//   important: false,
// })

// note.save().then(result => {
//   console.log('note saved!', result)
//   mongoose.connection.close()
// })

Note.find({important: true}).then(result => {
    result.forEach(note => {
        console.log(note);
    });

    mongoose.connection.close();
})