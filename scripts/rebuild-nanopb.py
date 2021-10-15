Import("env")

env.AddCustomTarget(
    name="nanopb",
    dependencies=None,
    actions=[
       " (cd proto; "
       "python ../.pio/libdeps/nanopb-example/Nanopb/generator/nanopb_generator.py  "
       "--strip-path --output-dir=../src simple.proto)"
    ],
    title="Nanopb generate step",
    description="Rebuild .c/.h files from .proto"
    #always_build=True
)