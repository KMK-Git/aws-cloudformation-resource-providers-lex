# CustomResource::Lex::Intent InputContext

The name of a context that must be active for an intent to be selected by Amazon Lex.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Name

The name of the context.

_Required_: Yes

_Type_: String

_Pattern_: <code>^([A-Za-z]_?){1,101}$</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

