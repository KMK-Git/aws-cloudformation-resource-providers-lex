# CustomResource::Lex::Intent SlotDefaultValue

A default value for a slot.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultvalue" title="DefaultValue">DefaultValue</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#defaultvalue" title="DefaultValue">DefaultValue</a>: <i>String</i>
</pre>

## Properties

#### DefaultValue

The default value for the slot. You can specify one of the following:
+ #context-name.slot-name - The slot value "slot-name" in the context "context-name."
+ {attribute} - The slot value of the session attribute "attribute."
+ 'value' - The discrete value "value."

_Required_: Yes

_Type_: String

_Minimum_: <code>1</code>

_Maximum_: <code>202</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

