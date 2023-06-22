# Compile smart contract

In the `algohub-pyteal` directory, clone the repository `algokit-pyteal-course` from AlgoHUB. It contains some materials that will help us along the course

```bash
git clone https://github.com/Algo-Hub-io/algokit-pyteal-course.git
```

## Compile beaker-pyteal smart contract

Now, let's create a new folder in the `playground` directory for our smart contract and name it `counter`
![make_counter_folder](make_counter_folder.png)

Now, head to the `algokit-pyteal-course` directory that we just cloned and navigate to `Lab1` folder.

Find the `counter.py` file, copy and paste it into the **counter** folder in our `playground`

In the terminal, change directory into the **counter** folder

```bash
cd playground/counter
```

And compile the smart contract with

```bash
python3 counter.py
```

The contract after being compiled will produce 4 new files inside the `artifacts` folder
![compiled_contract](compiled_contract.png)

Those files will be used in the next module to deploy the smart contract.
