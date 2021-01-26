## Installing

Assuming you’ve already installed Node.js, create a directory to hold your application, and make that your working directory.

```
$ mkdir myapp
$ cd myapp
```

Use the `npm init` command to create a `package.json` file for your application. For more information on how package.json works, see Specifics of npm’s `package.json` handling.

```
$ npm init
```
or
```
$ yarn init
```

This command prompts you for a number of things, such as the name and version of your application. For now, you can simply hit RETURN to accept the defaults for most of them, with the following exception:

```
entry point: (index.js)
```

Enter `app.js`, or whatever you want the name of the main file to be. If you want it to be `index.js`, hit RETURN to accept the suggested default file name.

Now install Express in the myapp directory and save it in the dependencies list. For example:

```
$ npm install express --save
```
or
```
$ yarn add express --save
```

To install Express temporarily and not add it to the dependencies list:

```
$ npm install express --no-save
```
or
```
$ yarn add express --no-save
```

## Hellow World Example

```
const express = require('express')

const app = express()
const port = 3030

app.get('/' , (req, res) => {
    res.send("Hello OIL")
})

app.listen(port, () => {
    console.log(`App listenint to port http://localhost:${port}`)
})
```

This app starts a server and listens on port 3030 for connections. The app responds with “Hello World!” for requests to the root URL (/) or route. For every other path, it will respond with a 404 Not Found.

Runnig locally

```
node <filename>.js
```