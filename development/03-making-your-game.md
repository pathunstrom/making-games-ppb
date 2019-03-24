3. Leveling Up - AKA what you need to do - 17 min
    1. Scene management
    2. Sprite coordination
        1. Using tags
        2. Using types
        3. As parameters
        4. Using the event system for messages
    3. Extending the event system
        1. Creating events
        2. Extending events
    4. Building new subsystems ??
    5. Cameras
        1. Subclassing


- Transition
    - Enough about what ppb does for you. Let's talk about how to use this
      toolset.
- Sprites
    - Behaviors
        - update pattern
        - event handlers
    - Coordination
        - Sprites can spawn other sprites.
            - pass one to another via parameter
        - Using types
            - All events have the current scene attached
            - `get(kind=type)`
        - Using tags
            - `scene.add(my_sprite, tags=["danger"])`
            - `scene.get(tag="danger")`
        - Using messaging
            - Every handlers accepts a signal function
            - `signal(my_event)`
- The Camera
    - Subclassing to add event handlers
    - Zoom?
    - Screen shake (Just kidding)
- Scenes
    - A stack
    - Commands from existing scenes (or subsystems)
        - StartScene - adds to the stack
        - StopScene - pops from the stack
        - ReplaceScene - pops, then adds to the stack
    - Lifetime messages
        - SceneStarted
        - ScenePaused
        - SceneContinued
        - SceneStopped
- Events
    - Raising events
        - `signal(my_event)`
    - Creating new events
        - Dataclasses!
        - Just raise an instance of new class
    - Extending classes
        - `GameEngine.register(EventType, attribute_name, callable)`
        - on publish
            - Each attribute registered is called (without parameters)
            - The return value is set on the event
        - this can even be used to change default attributes (use caution!)
- Subsystems
    - ???