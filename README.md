# object-tracking

This is an OpenCV-based object Tracking program. This is an article focusing on how to learn the object tracking task as well as the principle and related introduction. So, not too much on the engineering side.

## Requirement

The code has used as few complex third-party libraries as possible, and tried to reduce the complexity of setting up the environment. However, there are still some required libraries that need to be imported:

- opencv-python           4.7.0.72
- numpy                   1.21.6

As a real-time face-swapping program, some necessary hardware is required, and the author's test environment is shown in the following table:

|CPU|GPU|Memory|OS|Camera|
|---|---|---|---|---|
|Intel(R) Core(TM) i7-1065G CPU @ 1.30GHz|Intel(R) Iris(R) Plus Graphics(Inessential)|16G|Windows 11|build-in(Essential)|

## How to Use

1. Clone the code from Github.
2. Run: `python run.py -t kcf`.

The `target` is the only parameter that specifies the tracker. Defualt tracker is kcf. The full list is as follows:

- boosting: BOOSTING Tracker is slow and doesn't perform well, but it's worth mentioning as an "elder".
- mil: MIL Tracker is more accurate than BOOSTING Tracker, but with a higher failure rate.
- kcf: KCF Tracker is faster than both BOOSTING and MIL, but performs poorly in the presence of occlusion.
- csrt: CSRT Tracker is more accurate than KCF, but slower.
- medianflow: MedianFlow Tracker performs well in reporting errors, but the model fails for fast jumping or fast moving objects.
- tld: The false positives of TLD Tracker are very high, so it is not recommended.
- mosse: MOSSE Tracker is very fast, but not as accurate as CSRT and KCF.

## Principle

### The need of Tracking

Tracking is faster than Detection:

## License and Citations

The source code is published under MIT license, see [license file](./LICENSE) for details.