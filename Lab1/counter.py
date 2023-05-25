import beaker as bk
import pyteal as pt

class MyState:
    counter = bk.GlobalStateValue(pt.TealType.uint64)

    # 1. Add local state

# 2. Update App Name
app = bk.Application("Counter", state=MyState())

# 3. Add optin method

# 4. rename add and deduct to add_global and deduct_global
@app.external
def add(*, output: pt.abi.Uint64) -> pt.Expr:
    current_counter = app.state.counter
    result = current_counter + pt.Int(1)
    return pt.Seq(
        app.state.counter.set(result),
        output.set(current_counter)
    )

@app.external
def deduct(*, output: pt.abi.Uint64) -> pt.Expr:
    current_counter = app.state.counter
    result = current_counter - pt.Int(1)
    return pt.Seq(
        app.state.counter.set(result),
        output.set(current_counter)
    )

# 5. create a local version of add and deduct

@app.external(read_only=True)
def read_counter(*, output: pt.abi.Uint64) -> pt.Expr:
    return output.set(app.state.counter)

if __name__ == "__main__":
    spec = app.build()
    spec.export("artifacts")