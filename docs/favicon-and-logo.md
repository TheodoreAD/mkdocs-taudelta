# Favicon and Logo

## General considerations

The preferred `favicon` and `logo` source is a `vector format` image.
The preferred workflow is to create a `logo.svg` and convert it to `.ico` to obtain `favicon.ico`.

The preferred format is:

- `.svg` for `vector format` images
- `.png` for `raster format` images

The ideal canvas size is `256x256` pixels such that
both the `.svg` and the `.ico` files maintain quality at all sizes.
The ideal image is a shape that is discernible at a size of `32x32`,
clear at `48x48`, sharp at `128x128` pixels and perfect at `256x256` pixels.

## Obtaining the image

### Vector format image sources

Creating good images is difficult, putting them together not so much.

[Wikimedia Commons][wikimedia] is a good source of free .svg images and can be found [here][wikimedia].

[Vecteezy][vecteezy] is another good source of .svg images,
although not all are free, and can be found [here][vecteezy].

[wikimedia]: https://commons.wikimedia.org/w/index.php?search=&title=Special:Search
[vecteezy]: https://www.vecteezy.com/

### Editing the image

The proposed solution is an online editor.

!!! example "SVG Edit"
    `SVG Edit` is a JavaScript-driven `.svg` drawing editor that works in any modern browser.

    It is an open source project. Its [repository][svg-edit-repo] can be found [here][svg-edit-repo].
    Its [web application][svg-edit-app] can be found [here][svg-edit-app].

!!! example "Method Draw"
    `Method Draw` is a fork of `SVG Edit`.
    It removes some features in exchange for improved usability and user experience.

    Its [repository][method-draw-repo] can be found [here][method-draw-repo].
    Its [web application][method-draw-app] can be found [here][method-draw-app].

!!! example "Vectr"
    Vectr is a free web and desktop cross-platform graphics software
    used to create vector graphics easily and intuitively.

    Its [web application][vectr-app] can be found [here][vectr-app].

[svg-edit-repo]: https://github.com/SVG-Edit/svgedit
[svg-edit-app]: https://svg-edit.github.io/svgedit/releases/latest/editor/svg-editor.html
[method-draw-repo]: https://github.com/duopixel/Method-Draw
[method-draw-app]: https://editor.method.ac/
[vectr-app]: https://vectr.com/new

## Creating the .ico file

### From an existing image

Out of a number of tested sites, the best results (anti-aliased, clutter-free
one file output unlike [a complex favicon generator site][realfavicongenerator])
were obtained from the following:

- for `vector format`, [CONVERTICO for .svg files][convertico-svg] can be found [here][convertico-svg]
  and will produce a white background `.ico` file for transparent background sources
- for `raster format`, [CONVERTICO for .png files][convertico-png] can be found [here][convertico-png]
  and will produce a transparent background `.ico` file for transparent background sources

If you need a transparent background, it is best to work in `.svg` format
and convert the resulting image to the `.png` format.
A simple and ad-free [online converter][cloudconvert-svg-to-png] can be found [here][cloudconvert-svg-to-png].

### From scratch

To design your own `.ico` file pixel by pixel,
an [online editor][favicon-designer] can be found [here][favicon-designer].

[realfavicongenerator]: https://realfavicongenerator.net/
[convertico-svg]: https://convertico.com/svg-to-ico/
[convertico-png]: https://convertico.com/
[favicon-designer]: https://www.favicon.cc/
[cloudconvert-svg-to-png]: https://cloudconvert.com/svg-to-png
