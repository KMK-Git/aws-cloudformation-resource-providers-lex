# CustomResource::Lex::Intent Prompt

Obtains information from the user. To define a prompt, provide one or more messages and specify the number of attempts to get information from the user. If you provide more than one message, Amazon Lex chooses one of the messages to use to prompt the user. For more information, see [Amazon Lex: How It Works](https://docs.aws.amazon.com/lex/latest/dg/how-it-works.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#maxattempts" title="MaxAttempts">MaxAttempts</a>" : <i>Integer</i>,
    "<a href="#messages" title="Messages">Messages</a>" : <i>[ <a href="message.md">Message</a>, ... ]</i>,
    "<a href="#responsecard" title="ResponseCard">ResponseCard</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#maxattempts" title="MaxAttempts">MaxAttempts</a>: <i>Integer</i>
<a href="#messages" title="Messages">Messages</a>: <i>
      - <a href="message.md">Message</a></i>
<a href="#responsecard" title="ResponseCard">ResponseCard</a>: <i>String</i>
</pre>

## Properties

#### MaxAttempts

The number of times to prompt the user for information.

_Required_: Yes

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Messages

_Required_: Yes

_Type_: List of <a href="message.md">Message</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseCard

A response card. Amazon Lex uses this prompt at runtime, in the PostText API response. It substitutes session attributes and slot values for placeholders in the response card. For more information, see [Using a Response Card](https://docs.aws.amazon.com/lex/latest/dg/ex-resp-card.html).

_Required_: No

_Type_: String

_Minimum_: <code>1</code>

_Maximum_: <code>50000</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

