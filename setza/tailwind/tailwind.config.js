module.exports = {
  content: [
    "../templates/**/*.html",
    "../apps/**/*.py",
  ],
  theme: {
    extend: {
      colors: {
        canvas: "#f7f6f4",
        ink: "#111111",
        muted: "#7b756f",
        line: "#dedad6",
        surface: "#ffffff",
        soft: "#f2f0ed",
      },
      fontFamily: {
        sans: ["Manrope", "Inter", "Segoe UI", "sans-serif"],
      },
    },
  },
  plugins: [],
};
