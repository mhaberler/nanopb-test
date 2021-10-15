Import("env")


def nanopb_callback(*args, **kwargs):
    print("Hello PlatformIO!")
    env.SetDefault(NANOPB = "lib/nanopb")
    env.Tool("nanopb", toolpath = ["lib/nanopb/tests/site_scons/site_tools"])
    env.NanopbProto("proto/simple.proto")


env.AddCustomTarget(
    name="nanopb-scons",
    dependencies=None,
    actions=[
        "python --version", nanopb_callback
    ],
    title="Nanopb generate step, Scons flavor",
    description="Rebuild .c/.h files from .proto"
    #always_build=True
)