# name=Basic MIDI Keyboard
# url=TODO
"""
Basic MIDI Keyboard Script for FL Studio

This is a simple script for basic MIDI keyboards. It handles:
- MIDI note events (notes are handled automatically by FL Studio)
- Optional transport controls (if your keyboard has buttons)

To customize this script:
1. Press buttons/keys on your keyboard and check the script output
2. Note the status, data1, and data2 values for each control
3. Update the button mappings below to match your keyboard

Authors:
- Your Name
"""

import transport
import midi


def OnInit():
    """
    Called when FL Studio initializes the script.
    """
    print("Basic MIDI Keyboard script initialized")
    print("Press keys/buttons on your keyboard to see their MIDI values")


def OnDeInit():
    """
    Called when FL Studio de-initializes the script.
    """
    print("Basic MIDI Keyboard script de-initialized")


def OnMidiIn(event):
    """
    Called whenever your MIDI keyboard sends a message to FL Studio.
    
    MIDI note events (for playing notes) are handled automatically by FL Studio,
    so you don't need to handle them unless you want custom behavior.
    """
    
    # Check if this is a note event (note on or note off)
    # FL Studio handles these automatically, so we can let them pass through
    if event.status == midi.MIDI_NOTEON or event.status == midi.MIDI_NOTEOFF:
        # Notes are handled automatically - you can add custom logic here if needed
        # For example, you could add velocity scaling, note filtering, etc.
        pass
    
    # TRANSPORT CONTROLS
    # Uncomment and modify these based on your keyboard's button MIDI values
    # To find the values, press a button and check the script output
    
    # Example: Play/Pause button (modify status and data1 to match your keyboard)
    # if event.status == 191 and event.data1 == 115:
    #     if event.data2 > 0:  # Button pressed
    #         transport.start()
    #     event.handled = True
    
    # Example: Stop button
    # elif event.status == 191 and event.data1 == 116:
    #     if event.data2 > 0:
    #         transport.stop()
    #     event.handled = True
    
    # Example: Record button
    # elif event.status == 191 and event.data1 == 117:
    #     if event.data2 > 0:
    #         transport.record()
    #     event.handled = True
    
    # Example: Fast Forward button (hold to fast forward)
    # elif event.status == 191 and event.data1 == 113:
    #     if event.data2 > 0:
    #         transport.fastForward(2)  # Start fast forward
    #     else:
    #         transport.fastForward(0)  # Stop fast forward
    #     event.handled = True
    
    # Example: Rewind button (hold to rewind)
    # elif event.status == 191 and event.data1 == 112:
    #     if event.data2 > 0:
    #         transport.rewind(2)  # Start rewind
    #     else:
    #         transport.rewind(0)  # Stop rewind
    #     event.handled = True
    
    # DEBUG: Uncomment the line below to print all MIDI events
    # This is useful for finding the MIDI values of your keyboard's controls
    # print(f"Event: status={event.status:3}, data1={event.data1:3}, data2={event.data2:3}, handled={bool(event.handled)}")


def OnNoteOn(event):
    """
    Called when a note-on event is received.
    
    This is called before OnMidiIn. If you handle the event here and set
    event.handled = True, OnMidiIn won't be called for this event.
    """
    # Example: You could add custom note processing here
    # For instance, velocity scaling or note filtering
    pass


def OnNoteOff(event):
    """
    Called when a note-off event is received.
    
    This is called before OnMidiIn. If you handle the event here and set
    event.handled = True, OnMidiIn won't be called for this event.
    """
    # Example: You could add custom note-off processing here
    pass


def OnControlChange(event):
    """
    Called when a control change (CC) event is received.
    
    This is useful for handling knobs, sliders, and buttons that send CC messages.
    """
    # Example: Handle a specific CC number (modify to match your keyboard)
    # if event.data1 == 1:  # CC number 1 (usually mod wheel)
    #     # Do something with the CC value (event.data2)
    #     print(f"CC {event.data1} = {event.data2}")
    #     event.handled = True
    
    pass
