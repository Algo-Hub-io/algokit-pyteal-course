# Modify and deploy the counter app

In [Lab 2](../Lab2/README.md), we deployed a precompiled simple counter app.

The app stored the counter in global schema, but can cause some issues.

As the count is stored in the global schema, that means that the same counter is shared by anyone who interacts with the application, which reduces the usability for you as an individual.

So for this exercise, we will be adding a locally stored count (this means that it is stored locally with your account, and not locally on your machine).

When we are done, there will be both a global count and a local count in the smart contract.

To get started, open the AlgoKit `playground` project folder that we created in Lab 1. We will need to modify the `counter.py` file in the counter folder.

Let's open and start modifying the `counter.py` file.

The first item, we need to create a local state for the local account. This is a state value specific to each account that opt in to the smart contract (marked in comments by `# 1`).

```python
# 1 - add local state
local_counter = bk.LocalStateValue(
        stack_type=pt.TealType.uint64,
        default=pt.Int(0),
        descr="An int stored for each account that opts in",
    )
```

Secondly, we want to edit is the name, so update the name (again, marked by `# 2` in the file).

```python
"""Modified Counter Application"""
```

The next part we need to add `opt_in` method. This is because now we are using local state, all accounts will need to opt in to the application (marked by `# 3` in the file).

```python
# 3. Add optin method
@app.opt_in
def opt_in() -> pt.Expr:
    return app.initialize_local_state()
```

Next, we need to rename the add and deduct methods to be add_global and deduct_global (this is marked as `# 4` in comments).

Then we create a local version of the add and deduct methods.

That looks something like this

```python
    @app.external
    def add_local() -> pt.Expr:
        return app.state.local_counter.increment(pt.Int(1))

    @app.external
    def deduct_local() -> pt.Expr:
        return app.state.local_counter.decrement(pt.Int(1))
```

There is not much of differences we can see from using the global data schema, the beaker framework simplify the interaction with the local state in smart contracts. We can also see that we can use `increment()` and `decrement()` methods to add and deduct the integer value by a certain number.

We can see from above that we have updated the global function calls, and added new local calls.

Once that's done, we can compile our project files using the command `python3 counter.py`.

Deploy the compiled smart contract to Algorand Testnet following the same steps in [Lab 2](../Lab2/testnetDeploy.md)
