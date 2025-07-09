<template>
  <div>
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
