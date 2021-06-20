# CustomResource::Lex::Intent Statement

A collection of messages that convey information to the user. At runtime, Amazon Lex selects the message to convey.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#messages" title="Messages">Messages</a>" : <i>[ <a href="message.md">Message</a>, ... ]</i>,
    "<a href="#responsecard" title="ResponseCard">ResponseCard</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#messages" title="Messages">Messages</a>: <i>
      - <a href="message.md">Message</a></i>
<a href="#responsecard" title="ResponseCard">ResponseCard</a>: <i>String</i>
</pre>

## Properties

#### Messages

A collection of message objects.

_Required_: Yes

_Type_: List of <a href="message.md">Message</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseCard

At runtime, if the client is using the PostText API, Amazon Lex includes the response card in the response. It substitutes all of the session attributes and slot values for placeholders in the response card.

_Required_: No

_Type_: String

_Minimum_: <code>1</code>

_Maximum_: <code>50000</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

