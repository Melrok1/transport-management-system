<template>
  <div class="date-picker">
    <label>{{ label }}</label>
		<input
			type="date"
			:value="modelValue"
			@input="$emit('update:modelValue', ($event.target as HTMLInputElement).value)"
			/>
  </div>
</template>

<script setup lang="ts">

import { defineProps } from 'vue'

const props = defineProps<{
  modelValue: string
  label: string
}>()

</script>

<style scoped lang="scss">

.date-picker {
	display: flex;
	flex-direction: column;
	margin-bottom: 1rem;

	label {
		margin-bottom: 0.5rem;
	}

	input[type="date"] {
		padding: 0.5rem;
		border: 1px solid #ccc;
		border-radius: 4px;
		font-size: 1rem;
	}
}

</style>
