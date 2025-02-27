const mongoose = require('mongoose');

// if (process.argv.length<3) {
//     console.log('give password as argument')
//     process.exit(1)
// }

// const password = encodeURIComponent(process.argv[2]);
// console.log(password)
const url =
  'mongodb+srv://fullstack:Pikachu18%40@cluster0.2psjv.mongodb.net/testNoteApp?retryWrites=true&w=majority&appName=Cluster0'

mongoose.set('strictQuery',false)

mongoose.connect(url)

const noteSchema = new mongoose.Schema({
    content: String,
    important: Boolean,
})

const Note = mongoose.model('Note', noteSchema)

// const note = new Note({
//     'content': 'HTML is easy',
//     'important': true,
// })



// note.save().then(result => {
//     console.log('note saved!', result)
//     mongoose.connection.close()
// })

const note1 = new Note({
    'content': 'CSS is easy',
    'important': true
})

note1.save().then(result => {
    console.log('note saved!', result)
    mongoose.connection.close()
})

// Note.find({ important: true }).then(result => {
//     result.forEach(note => {
//         console.log(note);
//     });

//     mongoose.connection.close();
// })

// [
//     {
//       "content": "HTML is easy",
//       "important": true,
//       "id": "67b0b92115d7a11ce3e9294a"
//     },
//     {
//       "content": "CSS is easy",
//       "important": true,
//       "id": "67b0ba785df684732003a99b"
//     },
//     {
//       "content": "Mongose makes thing easy",
//       "important": false,
//       "id": "67b0bb392b7151d9fb02b609"
//     },
//     {
//       "content": "postman is good for testing...",
//       "important": true,
//       "id": "67bb7778b8f1e50590785ce1"
//     }
//   ]