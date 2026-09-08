
************************************
Documenting New Features and Changes
************************************

With every Blender release, exciting new features, improvements, and changes are introduced. To ensure Blender users
can make the most of these updates, the documentation needs to be updated in parallel.

The Blender documentation project tracks changes requiring updates or additions to the manual. By contributing, you
help keep the manual accurate and valuable for the global Blender community.

This guide will walk you through the process of documenting these changes using release issues and commit logs.


Using Release Issues to Track Changes
-------------------------------------

Each Blender release has an associated issue in the documentation project's
`Upcoming Releases Project <https://projects.blender.org/blender/blender-manual/projects/28>`__. These issues contains
a curated list of code commits from Blender's development process that introduce user-facing changes. These changes
typically require updates to the manual, such as new sections, modified instructions, or updated screenshots.

.. rubric:: Steps to Contribute

#. **Locate the Release Issue**:

   - Navigate to the documentation project's issue tracker and open the issue for the current or upcoming Blender
     release.
   - Review the list of commits provided in the issue description. Each commit represents a change or feature that
     needs documentation.

#. **Pick a Commit**:

   - Select a commit that interests you or aligns with your expertise. For example, if you're familiar with modeling
     tools, pick a change related to those features.
   - Make sure no one else is already working on the same task by checking the comments or status updates in the
     issue.

#. **Understand the Change**:

   - **Read the Commit Message**:

     Commit messages often summarize the purpose and scope of the change. They might link to a pull request (PR) or
     contain related discussion links.
   - **Check the PR or Code**:

     The linked PR provides additional context, including descriptions, images, or videos explaining the feature.
     Reviewing the code changes can also help you understand how the feature works.
   - **Test the Feature**:

     Open Blender and test the feature to see it in action. This hands-on experience will clarify how the feature
     behaves and how users will interact with it.

#. **Reach Out if Needed**:

   - If the commit message or PR doesn't provide enough information, you can:

     - Contact the developer of the change (their username is typically in the PR).
     - Ask questions on Blender's development channels or forums.


Key Considerations for Documentation
====================================

When documenting a change, keep the following in mind:

- **What's the Purpose?**:

  Understand why the change was made. Does it improve usability, introduce a new capability, or fix a problem?

- **Who Benefits?**:

  Consider the target audience for the feature. Is it meant for animators, modelers, or another user group?

- **How Does It Work?**:

  Write clear, concise instructions. Include practical examples or use cases when possible.

- **Look for Dependencies**:

  Some changes might depend on other features or affect existing functionality. Check if the change impacts other
  parts of the manual.

- **Screenshots and Visuals**:

  If the change affects Blender's interface, capture screenshots to illustrate it. Ensure visuals reflect the correct
  version of Blender.


Submitting Your Work
====================

Once you've drafted the documentation:

#. **Write in the Manual Style**:

   Follow the Blender documentation style guide to ensure clarity and consistency.

#. **Submit Your Contribution**:

   - :doc:`Open a pull request </contribute/manual/getting_started/local_editing/pull_requests>`
     in the documentation project.
   - Reference the release issue and the commit in your PR description.
   - Include any screenshots, diagrams, or examples you've created.

#. **Collaborate**:

   Work with the review team to refine your documentation until it's ready to publish.


Every Contribution Matters
==========================

Contributing to Blender's documentation is a rewarding way to support the community and ensure users understand the
latest features. By documenting these changes, you play a key role in making Blender more accessible and enjoyable for
everyone.

Start exploring the release issues today, and help bring Blender's innovations to life!
