# CustomResource::Lex::SlotType RegexConfiguration

A regular expression used to validate the value of a slot.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#pattern" title="Pattern">Pattern</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#pattern" title="Pattern">Pattern</a>: <i>String</i>
</pre>

## Properties

#### Pattern

A regular expression used to validate the value of a slot.

Use a standard regular expression. Amazon Lex supports the following characters in the regular expression:
+ A-Z, a-z
+ 0-9
+ Unicode characters ("\ u<Unicode>")
Represent Unicode characters with four digits, for example "\u0041" or "\u005A".

The following regular expression operators are not supported:
* Infinite repeaters: *, +, or {x,} with no upper bound.
* Wild card (.)

_Required_: Yes

_Type_: String

_Minimum_: <code>1</code>

_Maximum_: <code>100</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

