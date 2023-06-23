# Modify the Counter App template to work with your app

For this tutorial, we have modified a basic version of the `create-react-app` template to support working with Pera Wallet and Algorand.

To start with, we need to clone the repository for the template.

```bash
git clone https://github.com/Algo-Hub-io/counter-app.git
```

This will download the counter app template to our local machine.

Next we open it in our code editor, you can either do this by opening the app and selecting the directory, or you can do it from the command line (if you are using visual studio code and have installed the console prompt)

```bash
cd counter-app
code .
```

In the `counter-app` repository, navigate to `src/App.js`. We need to put our deployed smart contract in the code on line 14

```javascript
// The app ID on testnet
const appIndex = /* paste your smart contract id here*/;
```

Make sure the change is saved. Now we open the terminal in VS Code and run the following command one after another

```bash
# Install dependencies and packages
npm i

# Run the application
npm start
```
