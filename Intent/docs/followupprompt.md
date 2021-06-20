# CustomResource::Lex::Intent FollowUpPrompt

A prompt for additional activity after an intent is fulfilled. For example, after the OrderPizza intent is fulfilled, you might prompt the user to find out whether the user wants to order drinks.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#prompt" title="Prompt">Prompt</a>" : <i><a href="prompt.md">Prompt</a></i>,
    "<a href="#rejectionstatement" title="RejectionStatement">RejectionStatement</a>" : <i><a href="statement.md">Statement</a></i>
}
</pre>

### YAML

<pre>
<a href="#prompt" title="Prompt">Prompt</a>: <i><a href="prompt.md">Prompt</a></i>
<a href="#rejectionstatement" title="RejectionStatement">RejectionStatement</a>: <i><a href="statement.md">Statement</a></i>
</pre>

## Properties

#### Prompt

_Required_: Yes

_Type_: <a href="prompt.md">Prompt</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RejectionStatement

_Required_: Yes

_Type_: <a href="statement.md">Statement</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

