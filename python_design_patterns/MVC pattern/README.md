# Model-View-Controller pattern

One of the design principles related to software engineering is the separation of concerns
(SoC) principle. The idea behind the SoC principle is to split an application into distinct
sections, where each section addresses a separate concern. Examples of such concerns are
the layers used in a layered design (data access layer, business logic layer, presentation
layer, and so forth). Using the SoC principle simplifies the development and maintenance
of software applications.



The model is the core component. It represents knowledge. It contains and manages the
(business) logic, data, state, and rules of an application. The view is a visual representation
of the model. Examples of views are a computer GUI, the text output of a computer
terminal, a smartphone's application GUI, a PDF document, a pie chart, a bar chart, and so
forth. The view only displays the data; it doesn't handle it. The controller is the link/glue
between the model and view. All communication between the model and the view happens
through a controller.



A model is considered smart because it does the following:
+ Contains all the validation/business rules/logic
+ Handles the state of the application
+ Has access to application data (database, cloud, and so on)
+ Does not depend on the UI


A controller is considered thin because it does the following:
+ Updates the model when the user interacts with the view
+ Updates the view when the model changes
+ Processes the data before delivering it to the model/view, if necessary
+ Does not display the data
+ Does not access the application data directly
+ Does not contain validation/business rules/logic


A view is considered dumb because it does the following:
+ Displays the data
+ Allows the user to interact with it
+ Does only minimal processing, usually provided by a template language (for
+ example, using simple variables and loop controls)
+ Does not store any data
+ Does not access the application data directly
+ Does not contain validation/business rules/logic