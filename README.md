# MyFigure Module

A class for standardized accessible scientific plots.

## Overview
MyFigure is a Python module tailored for creating and customizing sophisticated visualizations with Matplotlib and Seaborn. It offers an intuitive interface to streamline figure setup, axis configuration, and style management, making it ideal for both simple plots and complex graphical representations in publications and presentations.

## Features
- **Seaborn and Matplotlib Integration**: Leverages the advanced styling and plotting capabilities of both Seaborn and Matplotlib to produce beautiful, scientific-grade figures.
- **Default Keyword Arguments**: Supports easy customization and flexibility by allowing default configurations that can be overridden according to user needs.
- **Broadcast Keyword Arguments**: Automatically broadcasts single values across multiple axes or applies unique values per axis, enhancing customization without additional code for each axis.
- **Automatic Axis Management**: Always creates axes as a list, simplifying access and manipulation (e.g., `mf.axs[0]`), including support for `twinx` without raising exceptions.
- **Automatic Application of Hatches**: Applies hatch patterns to bars in bar plots automatically, improving visibility in colorblind-friendly and black-and-white printouts.
- **Annotate Outliers**: Offers functionality to annotate outliers to address scaling issues with a few outlying data points.
- **Edge Padding in Limits**: Automatically adds a 5% padding to `x_lim`, `y_lim`, and `yt_lim` to avoid the "Excel-effect" where lines touch the edges of the plot.
- **Legend Integration**: Seamlessly integrates legends from multiple axes and `twinx` in a unified view.
- **Consistent Subplot Annotations**: Automatically places letters or annotations in subplots to ensure consistent location across figures.
- **Label Rotation and Anchoring**: When labels on the x-axis are rotated, they are anchored on their right to enhance readability.
- **Mask Insignificant Data**: Temporarily masks data in bar plots where the error (standard deviation) is greater than the mean, applying a transparency effect to highlight significant results.
- **Inset Plots**: Simplifies the creation of inset plots within larger axes for detailed examinations of data subsets.
- **Flexible Saving Options**: Allows figures to be saved in various formats including PNG, PDF, SVG, EPS, and TIFF, with options for resolution settings and transparency. This provides versatility for different publishing needs and ensures high-quality outputs.

## Installation
Install MyFigure using pip:
```bash
pip install myfigure
```

## Examples 

Examples are available in the ``examples`` folder.
To run examples:
1. Install ``myfigure`` in your Python environment
2. Download or copy-paste the example code in your editor
3. Run the code 
4. If you run the scripts as Jupyter Notebooks, replace the relative path at the beginning of the example with the absolute path to the folder where you want to save the plots.

## How to use MyFigure inside functions
```bash
# minimum example of function that uses MyFigure to plot its results
def function_using_myfigure(
    your_other_parameters,
    **kwargs,
) -> MyFigure:

    # core computation of the function, to compute the data that
    # will need to be plotted using myfunction

    # if you want to specify a different out_path for the output of this function
    out_path = your_alternative_path  # (using plib)
    out_path.mkdir(parents=True, exist_ok=True)  # create the folder if missing

    # example of default parameter that are specific for this function
    default_kwargs = {
        "height": 4,  # this can be changed, but the default is 4
        "width": 4,  # this can be changed, but the default is 4
        "y_lab": "very_specific_y_lab",  # this can be changed, but the default is "very_specific_y_lab"
    }
    # Update kwargs with the default key-value pairs if the key is not present in kwargs
    kwargs = {**default_kwargs, **kwargs}

    myfig = MyFigure(
        rows=1,  # this cannot be modified, function_using_myfigure(rows=2) gives an error
        cols=1,  # this cannot be modified, function_using_myfigure(rows=2) gives an error
        **kwargs, # this ensures full customization of the object
    )
    myfig.save_figure()
    # it is advisable to return the object so that furter modificaiton can be performed
    # outside the function if needed (then calling again myfig.save_figure() will simply overwrite the
    # version of the figure since the output path is stored in myfig)
    return myfig


# how to call the function
mf_default = function_using_myfigure()  # with default values
# %%
mf_non_default = function_using_myfigure(
    x_lim=(0, 1), height=6, x_lab="a", y_lab="another_specific_label"
) # customized
#
mf = function_using_myfigure()
mf.axs[0].plot([1], [1])  # something that was impossible inside the function
mf.save_figure()
```