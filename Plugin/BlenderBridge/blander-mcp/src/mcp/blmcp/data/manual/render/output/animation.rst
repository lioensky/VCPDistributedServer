
********************
Rendering Animations
********************

While rendering stills will allow you to view and save the image from the render buffer when
it is complete, animations are a series of images, or frames,
and are automatically saved directly out to a drive after being rendered.

After rendering the frames, you may need to edit the clips,
or first use the Compositor to do green-screen masking, matting, color correction, DOF,
and so on to the images. That result is then fed to the Sequencer where the strips are cut and
mixed and a final overlay is done.

Finally you can render out from the Sequencer and compress the frames into a playable movie clip.


Workflow
========

Generally, you do a lot of intermediate renders of different frames in your animation to check
for timing, lighting, placement, materials, and so on. At some point,
you are ready to make a final render of the complete animation for publication.

There are two approaches you can use when making a movie, or animation, with or without sound.
The approach you should use depends on the amount of CPU time you will need to render the movie.
You can render a "typical" frame at the desired resolution,
and then multiply by the number of frames that will ultimately go into the movie, to arrive at a total render time.

If the total render time is an hour or more, you want to use the "Frame Sequence" approach.
For example, if you are rendering a one-minute video clip for film, there will be
(60 seconds per minute) X (24 frames per second) or 1440 frames per minute.
If each frame takes 30 seconds to render,
then you will be able to render two frames per minute, or need 720 minutes (12 hours)
of render time.

Rendering takes all available CPU time; you should render overnight,
when the computer is not needed, or set Blender to a low priority while rendering,
and work on other things (be careful with the RAM space!).


.. rubric:: Direct Approach

The Direct Approach, which is highly **not** recommended and not a standard practice,
is where you set your output format to an AVI or MOV format,
and click *Animation* to render your scene directly out to a movie file.
Blender creates one file that holds all the frames of your animation.
You can then use Blender's :doc:`Video Sequencer </editors/video_sequencer/index>`
to add an audio track to the animation and render out to an MPEG format to complete your movie.


.. rubric:: Frame Sequence

The Frame Sequence is a much more stable approach,
where you set your output format to a still format (such as JPG, PNG or a multi-layer format).
Click *Animation* to render your scene out to a set of images,
where each image is a frame in the sequence.

Blender creates a file for each frame of the animation.
You can then use Blender's Compositor to perform any frame manipulation (post-processing).
You can then use Blender's :doc:`Video Sequencer </editors/video_sequencer/index>` to load that final image sequence,
add an audio track to the animation, and render out to an MPEG format to complete your movie.
The Frame Sequence approach is a little more complicated and takes more drive space,
but gives you more flexibility.

Here are some guidelines to help you choose an approach.


.. rubric:: Direct Approach

- Short segments with total render time under one hour.
- Stable power supply.
- Computer not needed for other uses.


.. rubric:: Frame Sequence Approach

- Total render time over one hour.
- Post-production work needed:

  - Color/lighting adjustment
  - Green screen/matte replacement
  - Layering/compositing
  - Multiple formats and resolutions of the final product
- Intermediate frames/adjustments needed for compression/codec.
- Precise timing (e.g. lip-sync to audio track) needed in parts.
- May need to interrupt rendering to use the computer, and want to be able to resume rendering where you left off.


Frame Sequence Workflow
=======================

#. First prepare your animation.
#. In the *Format* panel, choose the render size, Pixel Aspect Ratio, and the Range of Frames to use,
   as well as the frame rate, which should already be set.
#. In the Output panel set up your animation to be rendered out as images,
   generally using a format that does not compromise any quality.
#. Choose the output path and file type in the Output panel as well, for example ``//render/my-anim-``.
#. Confirm the range of your animation (frame Start and End).
#. Save your blend-file.
#. Press the *Animation* button and once the animation is finished,
   use your file manager to navigate to the output folder (``render`` in this example).
   You will see lots of images that have a sequence number attached to. These are the single frames.
#. In Blender, open the :doc:`Video Sequencer </video_editing/index>`.

   .. note::

      The Video Sequencer does not support multi-layer EXR files.
      To render to a video format you will have to skip the next three steps and
      instead use an :doc:`Image Input node </compositing/types/input/image>`
      in the :doc:`Compositor </compositing/types/input/image>`.

#. Choose *Add Image* from the add menu. Select all the frames from your output folder that you want to include
   in your animation. They will be added as a strip in the Sequence editor.
#. Now you can edit the strip and add effects or leave it like it is.
   You can add other strips, like an audio strip.
#. Scrub through the animation to check if you have included all the frames.
#. In the Output panel, choose the container and codec you want (e.g. ``MPEG H.264``) and configure them.
   The video codecs are described in :doc:`Output Options </render/output/properties/output>`.
#. Click the *Animation* render button and Blender will render out the Sequence editor output into a movie.


Hints
=====

Your computer accidentally turns off in the middle of rendering your movie!
   Unless your animation renders in a few minutes,
   it is best to render the animation as separate image files.
   Instead of rendering directly to a compressed movie file, use a lossless format (e.g. ``PNG``).

   This allows you an easy recovery if there is a problem and you have to re-start the rendering,
   since the frames you have already rendered will still be in the output directory.

   Just disable the *Overwrite* option to start rendering where you left off.

   You can then make a movie out of the separate frames with Blender's Sequence editor
   or use 3rd party encoding software.

Animation Preview
   It can be useful to render a subset of the animated sequence,
   since only part of an animation may have an error.

   Using an image format for output,
   you can use the *Frame Step* option to render every *N'th* frame.
   Then disable *Overwrite* and re-render with *Frame Step* set to 1.
