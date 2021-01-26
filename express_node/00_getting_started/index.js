const express = require('express')

const app = express()
const port = 3030

app.get('/' , (req, res) => {
    res.send("Hello OIL")
})


app.listen(port, () => {
    console.log(`App listenint to port http://localhost:${port}`)
})