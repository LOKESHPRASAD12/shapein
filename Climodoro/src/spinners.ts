import ora, { Color } from "ora";

export function createSpinner(color: Color, text: string) {
  const spinner = ora(text);
  spinner.color = color;
  return spinner;
}