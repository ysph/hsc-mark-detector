# hsc-mark-detector
Finding dots via CV

## How it works

1. Detects the effective area
2. Calculates the value of each square which makes that area
3. Draws only dots corresponding to the initial picture
4. Creates gif frame by frame

## Usage

```bash
python main.cpp
```

## Expected result

- Each picture is redrawed into the processed one
- Coordinates of the dots on picture are printed into console
- The initial and the resulting GIFs are created

## Example
![Initial](https://github.com/ysph/hsc-mark-detector/blob/master/initial.gif)

![Fixed](https://github.com/ysph/hsc-mark-detector/blob/master/fixed.gif)