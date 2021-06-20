# CustomResource::Lex::Intent Slot

Identifies the version of a specific slot.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultvaluespec" title="DefaultValueSpec">DefaultValueSpec</a>" : <i><a href="slotdefaultvaluespec.md">SlotDefaultValueSpec</a></i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#obfuscationsetting" title="ObfuscationSetting">ObfuscationSetting</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Integer</i>,
    "<a href="#responsecard" title="ResponseCard">ResponseCard</a>" : <i>String</i>,
    "<a href="#sampleutterances" title="SampleUtterances">SampleUtterances</a>" : <i>[ String, ... ]</i>,
    "<a href="#slotconstraint" title="SlotConstraint">SlotConstraint</a>" : <i>String</i>,
    "<a href="#slottype" title="SlotType">SlotType</a>" : <i>String</i>,
    "<a href="#slottypeversion" title="SlotTypeVersion">SlotTypeVersion</a>" : <i>String</i>,
    "<a href="#valueelicitationprompt" title="ValueElicitationPrompt">ValueElicitationPrompt</a>" : <i><a href="prompt.md">Prompt</a></i>
}
</pre>

### YAML

<pre>
<a href="#defaultvaluespec" title="DefaultValueSpec">DefaultValueSpec</a>: <i><a href="slotdefaultvaluespec.md">SlotDefaultValueSpec</a></i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#obfuscationsetting" title="ObfuscationSetting">ObfuscationSetting</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>Integer</i>
<a href="#responsecard" title="ResponseCard">ResponseCard</a>: <i>String</i>
<a href="#sampleutterances" title="SampleUtterances">SampleUtterances</a>: <i>
      - String</i>
<a href="#slotconstraint" title="SlotConstraint">SlotConstraint</a>: <i>String</i>
<a href="#slottype" title="SlotType">SlotType</a>: <i>String</i>
<a href="#slottypeversion" title="SlotTypeVersion">SlotTypeVersion</a>: <i>String</i>
<a href="#valueelicitationprompt" title="ValueElicitationPrompt">ValueElicitationPrompt</a>: <i><a href="prompt.md">Prompt</a></i>
</pre>

## Properties

#### DefaultValueSpec

Contains the default values for a slot. Default values are used when Amazon Lex hasn't determined a value for a slot.

_Required_: No

_Type_: <a href="slotdefaultvaluespec.md">SlotDefaultValueSpec</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of the slot.

_Required_: No

_Type_: String

_Maximum_: <code>200</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the slot.

_Required_: Yes

_Type_: String

_Pattern_: <code>^([A-Za-z]_?){1,101}$</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObfuscationSetting

Determines whether a slot is obfuscated in conversation logs and stored utterances. When you obfuscate a slot, the value is replaced by the slot name in curly braces ({}). For example, if the slot name is "full_name", obfuscated values are replaced with "{full_name}". For more information, see [Slot Obfuscation](https://docs.aws.amazon.com/lex/latest/dg/how-obfuscate.html).

_Required_: No

_Type_: String

_Allowed Values_: <code>NONE</code> | <code>DEFAULT_OBFUSCATION</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Directs Amazon Lex the order in which to elicit this slot value from the user. For example, if the intent has two slots with priorities 1 and 2, AWS Amazon Lex first elicits a value for the slot with priority 1. If multiple slots share the same priority, the order in which Amazon Lex elicits values is arbitrary.

_Required_: No

_Type_: Integer

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseCard

A set of possible responses for the slot type used by text-based clients. A user chooses an option from the response card, instead of using text to reply. 

_Required_: No

_Type_: String

_Minimum_: <code>1</code>

_Maximum_: <code>50000</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SampleUtterances

 If you know a specific pattern with which users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy. This is optional. In most cases, Amazon Lex is capable of understanding user utterances.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotConstraint

Specifies whether the slot is required or optional.

_Required_: Yes

_Type_: String

_Allowed Values_: <code>Required</code> | <code>Optional</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotType

The type of the slot, either a custom slot type that you defined or one of the built-in slot types.

_Required_: No

_Type_: String

_Minimum_: <code>1</code>

_Maximum_: <code>100</code>

_Pattern_: <code>^((AMAZON\.)_?|[A-Za-z]_?)+</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotTypeVersion

The version of the slot type.

_Required_: No

_Type_: String

_Minimum_: <code>1</code>

_Maximum_: <code>64</code>

_Pattern_: <code>\$LATEST|[0-9]+</code>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueElicitationPrompt

_Required_: No

_Type_: <a href="prompt.md">Prompt</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

