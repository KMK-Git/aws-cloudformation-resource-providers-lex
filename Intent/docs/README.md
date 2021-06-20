# CustomResource::Lex::Intent

Resource schema for CustomResource::Lex::Intent

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "CustomResource::Lex::Intent",
    "Properties" : {
        "<a href="#conclusionstatement" title="ConclusionStatement">ConclusionStatement</a>" : <i><a href="statement.md">Statement</a></i>,
        "<a href="#confirmationprompt" title="ConfirmationPrompt">ConfirmationPrompt</a>" : <i><a href="prompt.md">Prompt</a></i>,
        "<a href="#createversion" title="CreateVersion">CreateVersion</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dialogcodehook" title="DialogCodeHook">DialogCodeHook</a>" : <i><a href="codehook.md">CodeHook</a></i>,
        "<a href="#followupprompt" title="FollowUpPrompt">FollowUpPrompt</a>" : <i><a href="followupprompt.md">FollowUpPrompt</a></i>,
        "<a href="#fulfillmentactivity" title="FulfillmentActivity">FulfillmentActivity</a>" : <i><a href="fulfillmentactivity.md">FulfillmentActivity</a></i>,
        "<a href="#inputcontexts" title="InputContexts">InputContexts</a>" : <i>[ <a href="inputcontext.md">InputContext</a>, ... ]</i>,
        "<a href="#kendraconfiguration" title="KendraConfiguration">KendraConfiguration</a>" : <i><a href="kendraconfiguration.md">KendraConfiguration</a></i>,
        "<a href="#outputcontexts" title="OutputContexts">OutputContexts</a>" : <i>[ <a href="outputcontext.md">OutputContext</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parentintentsignature" title="ParentIntentSignature">ParentIntentSignature</a>" : <i>String</i>,
        "<a href="#rejectionstatement" title="RejectionStatement">RejectionStatement</a>" : <i><a href="statement.md">Statement</a></i>,
        "<a href="#sampleutterances" title="SampleUtterances">SampleUtterances</a>" : <i>[ String, ... ]</i>,
        "<a href="#slots" title="Slots">Slots</a>" : <i>[ <a href="slot.md">Slot</a>, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: CustomResource::Lex::Intent
Properties:
    <a href="#conclusionstatement" title="ConclusionStatement">ConclusionStatement</a>: <i><a href="statement.md">Statement</a></i>
    <a href="#confirmationprompt" title="ConfirmationPrompt">ConfirmationPrompt</a>: <i><a href="prompt.md">Prompt</a></i>
    <a href="#createversion" title="CreateVersion">CreateVersion</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dialogcodehook" title="DialogCodeHook">DialogCodeHook</a>: <i><a href="codehook.md">CodeHook</a></i>
    <a href="#followupprompt" title="FollowUpPrompt">FollowUpPrompt</a>: <i><a href="followupprompt.md">FollowUpPrompt</a></i>
    <a href="#fulfillmentactivity" title="FulfillmentActivity">FulfillmentActivity</a>: <i><a href="fulfillmentactivity.md">FulfillmentActivity</a></i>
    <a href="#inputcontexts" title="InputContexts">InputContexts</a>: <i>
      - <a href="inputcontext.md">InputContext</a></i>
    <a href="#kendraconfiguration" title="KendraConfiguration">KendraConfiguration</a>: <i><a href="kendraconfiguration.md">KendraConfiguration</a></i>
    <a href="#outputcontexts" title="OutputContexts">OutputContexts</a>: <i>
      - <a href="outputcontext.md">OutputContext</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parentintentsignature" title="ParentIntentSignature">ParentIntentSignature</a>: <i>String</i>
    <a href="#rejectionstatement" title="RejectionStatement">RejectionStatement</a>: <i><a href="statement.md">Statement</a></i>
    <a href="#sampleutterances" title="SampleUtterances">SampleUtterances</a>: <i>
      - String</i>
    <a href="#slots" title="Slots">Slots</a>: <i>
      - <a href="slot.md">Slot</a></i>
</pre>

## Properties

#### ConclusionStatement

A collection of messages that convey information to the user. At runtime, Amazon Lex selects the message to convey.

_Required_: No

_Type_: <a href="statement.md">Statement</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfirmationPrompt

Obtains information from the user. To define a prompt, provide one or more messages and specify the number of attempts to get information from the user. If you provide more than one message, Amazon Lex chooses one of the messages to use to prompt the user. For more information, see [Amazon Lex: How It Works](https://docs.aws.amazon.com/lex/latest/dg/how-it-works.html).

_Required_: No

_Type_: <a href="prompt.md">Prompt</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateVersion

When set to true a new numbered version of the intent is created for each update.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of the intent.

_Required_: No

_Type_: String

_Minimum_: <code>1</code>

_Maximum_: <code>200</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DialogCodeHook

Specifies a Lambda function that verifies requests to a bot or fulfills the user's request to a bot.

_Required_: No

_Type_: <a href="codehook.md">CodeHook</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FollowUpPrompt

A prompt for additional activity after an intent is fulfilled. For example, after the OrderPizza intent is fulfilled, you might prompt the user to find out whether the user wants to order drinks.

_Required_: No

_Type_: <a href="followupprompt.md">FollowUpPrompt</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FulfillmentActivity

Describes how the intent is fulfilled after the user provides all of the information required for the intent. You can provide a Lambda function to process the intent, or you can return the intent information to the client application. We recommend that you use a Lambda function so that the relevant logic lives in the Cloud and limit the client-side code primarily to presentation. If you need to update the logic, you only update the Lambda function; you don't need to upgrade your client application.

Consider the following examples:
+ In a pizza ordering application, after the user provides all of the information for placing an order, you use a Lambda function to place an order with a pizzeria.
+ In a gaming application, when a user says "pick up a rock", this information must go back to the client application so that it can perform the operation and update the graphics. In this case, you want Amazon Lex to return the intent data to the client.

_Required_: No

_Type_: <a href="fulfillmentactivity.md">FulfillmentActivity</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InputContexts

An array of InputContext objects that lists the contexts that must be active for Amazon Lex to choose the intent in a conversation with the user.

_Required_: No

_Type_: List of <a href="inputcontext.md">InputContext</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KendraConfiguration

Provides configuration information for the AMAZON.KendraSearchIntent intent. When you use this intent, Amazon Lex searches the specified Amazon Kendra index and returns documents from the index that match the user's utterance. For more information, see AMAZON.KendraSearchIntent.

_Required_: No

_Type_: <a href="kendraconfiguration.md">KendraConfiguration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutputContexts

An array of OutputContext objects that lists the contexts that the intent activates when the intent is fulfilled.

_Required_: No

_Type_: List of <a href="outputcontext.md">OutputContext</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the intent. The name is not case sensitive. The name can't match a built-in intent name, or a built-in intent name with "AMAZON." removed. For example, because there is a built-in intent called AMAZON.HelpIntent, you can't create a custom intent called HelpIntent. For a list of built-in intents, see [Standard Built-in Intents](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents) in the Alexa Skills Kit.

_Required_: Yes

_Type_: String

_Pattern_: <code>^([A-Za-z]_?){1,101}$</code>

_Update requires_: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

#### ParentIntentSignature

A unique identifier for the built-in intent to base this intent on. To find the signature for an intent, see [Standard Built-in Intents](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents) in the Alexa Skills Kit.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RejectionStatement

_Required_: No

_Type_: <a href="statement.md">Statement</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SampleUtterances

An array of utterances (strings) that a user might say to signal the intent. For example, "I want {PizzaSize} pizza", "Order {Quantity} {PizzaSize} pizzas". In each utterance, a slot name is enclosed in curly braces.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slots

An array of intent slots. At runtime, Amazon Lex elicits required slot values from the user using prompts defined in the slots. For more information, see [Amazon Lex: How It Works](https://docs.aws.amazon.com/lex/latest/dg/how-it-works.html).

_Required_: No

_Type_: List of <a href="slot.md">Slot</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### Version

The version of the intent.

#### Checksum

Checksum of the $LATEST version of the intent.

#### CreatedDate

The date that the intent was created.

#### LastUpdatedDate

The date that the intent was updated. When you create a resource, the creation date and last update dates are the same.

