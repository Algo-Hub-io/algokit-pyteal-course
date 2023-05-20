import beaker as bk
import pyteal as pt

class MyState:
    counter = bk.GlobalStateValue(pt.TealType.uint64)

app = bk.Application("Counter", state=MyState())

@app.external
def add(*, output: pt.abi.Uint64) -> pt.Expr:
    current_counter = app.state.counter
    result = current_counter + pt.Int(1)
    return pt.Seq(
        app.state.counter.set(result),
        output.set(result)
    )

@app.external
def deduct(*, output: pt.abi.Uint64) -> pt.Expr:
    current_counter = app.state.counter
    result = current_counter - pt.Int(1)
    return pt.Seq(
        app.state.counter.set(result),
        output.set(result)
    )

@app.external(read_only=True)
def read_counter(*, output: pt.abi.Uint64) -> pt.Expr:
    return output.set(app.state.counter)

if __name__ == "__main__":
    spec = app.build()
    spec.export("artifacts")