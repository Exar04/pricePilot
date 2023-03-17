const express = require('express')
const mongoose = require('mongoose')

const app = express()

app.set('view engine', 'ejs')
app.listen(4000)

// middleware and static files

app.use(express.static('public'))
app.use(express.urlencoded({ extended: true}))


app.get('/', (req, res) => {
    res.render('index', { title : 'HOME'})
})

app.post('/', (req, res) => {
    console.log(req.body)
    res.redirect('/')
})

app.get('/about', (req, res) => {
    res.render('about', {title : 'About'})
})

app.get('/Wishlist', (req, res) => {
    res.render('Wishlist', {title : 'Wishlist'})
})

app.use((req, res) => {
    res.status(404).render('404', {title: 'ERROR'})
})