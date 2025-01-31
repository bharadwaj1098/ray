import ray
import time

ray.init(num_gpus=2)

ds = ray.experimental.data.range(100)


def preprocess(x):
    import time
    time.sleep(.1)
    return x


class Model:
    def __call__(self, x):
        time.sleep(.1)
        return x


ds = ds.pipeline(parallelism=10) \
    .map(preprocess) \
    .map(Model, compute="actors", num_gpus=1)

for x in ds.iter_rows():
    pass
