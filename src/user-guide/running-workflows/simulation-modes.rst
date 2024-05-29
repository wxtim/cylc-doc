.. _SimulationMode:

Run Modes
---------

The run modes described in :ref:`task-run-modes` can
be applied to the entire workflow.

This is useful when developing workflows. Tasks submitted
using :ref:`task-run-modes.dummy` and
:ref:`task-run-modes.simulation` pathways can be used while
developing workflows to understand how different outcomes
and run lengths will affect the workflow.

To apply a run mode to a workflow:

.. code-block:: console

   $ cylc play --mode=dummy <workflow-id>
   $ cylc play --mode=simulation <workflow-id>

.. note::

   If a task has a run-mode set using
   :cylc:conf:`[runtime][<namespace>]run mode`
   this will override any run mode set for the workflow
   on the command line.


Limitations
^^^^^^^^^^^

Workflow run mode is recorded in the workflow run database. Cylc will not let you
*restart* a dummy mode workflow in live mode, or vice versa. Instead,
install a new instance of the workflow and run it from scratch in the new mode.
