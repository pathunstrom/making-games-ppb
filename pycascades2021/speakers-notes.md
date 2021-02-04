1. Introduction - no more than 4 minutes
    1. Welcome
    2. Who Am I?
        - Me
        - Position
        - Open Source
    3. This Talk
        1. Introduction to the building blocks of ppb
        2. Goals:
            - By the end, you should feel comfortable experimenting on your own game
            - How to think about game creation
            - Understanding Events and the event loop
            - The purpose of and use of Scenes
            - Whats the difference between Sprites and GameObjects
2. Getting Started
    1. Why ppb?
        - elevator pitch about education focus
        - key benefits for a dev focused audience
            - Easy to get started
            - It lets you solve the problems you care about
            - Deeply extensible
    2. So how fast can you get started?
        - ppb.run()
        - keyword arguments that matter here: setup and starting_scene
            - setup is a callable that accepts a ppb Scene
                - think of it like an init function!
            - starting_scene is the class that is instantiated before passed to setup
            - This flexibility allows you to progressively grow the complexity of your initialization.
3. Sprites and Events:
    1. Sprites
        - visible game objects
        - Can take arbitrary keyword arguments
        - Rendered
            - use the image attribute to change their look
            - rendered centered on their position attribute
            - used sprite.rotation to rotate the image
            - uses the sprite's dimensions to determine their size
        - Making them move using events
        - The shape of an event handler
    2. Events
        1. What are events?
            * A thing happened, or should happen
            * A brief list of ppb defined events
        2. Defining events
            - dataclasses!
        3. Emitting events
            - Signal function
            - parameters are an event instance and targets
            - Good for communication between game objects!
4. Scenes and GameObjects:
    1. So let's swap from a setup function to a scene
    2. What are Scenes?
        - Conceptually "parts" of a game
        - If the layout of a section is significantly different
            - menus, credits, different levels
        - Containers
    3. How you should use them
        - Every menu, splash screen, or level of your game is its own scene
        - Don't worry about reused code for your first game or six.
        - 
5. Systems (Very quick)
    - systemslib
    - exercise of the watcher
6. The end
    1. Summary
    2. 