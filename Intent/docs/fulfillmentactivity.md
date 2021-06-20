# CustomResource::Lex::Intent FulfillmentActivity

Describes how the intent is fulfilled after the user provides all of the information required for the intent. You can provide a Lambda function to process the intent, or you can return the intent information to the client application. We recommend that you use a Lambda function so that the relevant logic lives in the Cloud and limit the client-side code primarily to presentation. If you need to update the logic, you only update the Lambda function; you don't need to upgrade your client application.

Consider the following examples:
+ In a pizza ordering application, after the user provides all of the information for placing an order, you use a Lambda function to place an order with a pizzeria.
+ In a gaming application, when a user says "pick up a rock", this information must go back to the client application so that it can perform the operation and update the graphics. In this case, you want Amazon Lex to return the intent data to the client.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#codehook" title="CodeHook">CodeHook</a>" : <i><a href="codehook.md">CodeHook</a></i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#codehook" title="CodeHook">CodeHook</a>: <i><a href="codehook.md">CodeHook</a></i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### CodeHook

_Required_: No

_Type_: <a href="codehook.md">CodeHook</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

 How the intent should be fulfilled, either by running a Lambda function or by returning the slot data to the client application.

_Required_: Yes

_Type_: String

_Allowed Values_: <code>ReturnIntent</code> | <code>CodeHook</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

