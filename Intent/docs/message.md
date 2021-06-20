# CustomResource::Lex::Intent Message

The message object that provides the message text and its type.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#content" title="Content">Content</a>" : <i>String</i>,
    "<a href="#contenttype" title="ContentType">ContentType</a>" : <i>String</i>,
    "<a href="#groupnumber" title="GroupNumber">GroupNumber</a>" : <i>Integer</i>
}
</pre>

### YAML

<pre>
<a href="#content" title="Content">Content</a>: <i>String</i>
<a href="#contenttype" title="ContentType">ContentType</a>: <i>String</i>
<a href="#groupnumber" title="GroupNumber">GroupNumber</a>: <i>Integer</i>
</pre>

## Properties

#### Content

The text of the message.

_Required_: Yes

_Type_: String

_Minimum_: <code>1</code>

_Maximum_: <code>1000</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentType

The content type of the message string.

_Required_: Yes

_Type_: String

_Allowed Values_: <code>PlainText</code> | <code>SSML</code> | <code>CustomPayload</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupNumber

Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.

_Required_: No

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

