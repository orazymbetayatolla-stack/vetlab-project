(function () {
  const KEY = "a11ySettings";

  const defaults = {
    on: false,
    font: "base",          // base | lg | xl
    contrast: false,
    underline: false,
    spacing: false,
    reduceMotion: false
  };

  function load() {
    try {
      return { ...defaults, ...(JSON.parse(localStorage.getItem(KEY)) || {}) };
    } catch {
      return { ...defaults };
    }
  }

  function save(s) {
    localStorage.setItem(KEY, JSON.stringify(s));
  }

  function apply(s) {
    const b = document.body;

    b.classList.toggle("a11y-on", !!s.on);

    b.classList.remove("a11y-font-lg", "a11y-font-xl");
    if (s.on && s.font === "lg") b.classList.add("a11y-font-lg");
    if (s.on && s.font === "xl") b.classList.add("a11y-font-xl");

    b.classList.toggle("a11y-contrast", !!(s.on && s.contrast));
    b.classList.toggle("a11y-underline", !!(s.on && s.underline));
    b.classList.toggle("a11y-spacing", !!(s.on && s.spacing));
    b.classList.toggle("a11y-reduce-motion", !!(s.on && s.reduceMotion));

    // aria-pressed на кнопке
    const toggleBtn = document.getElementById("a11yToggle");
    if (toggleBtn) toggleBtn.setAttribute("aria-pressed", s.on ? "true" : "false");

    // Показ/скрытие кнопки настроек
    const settingsBtn = document.getElementById("a11ySettingsBtn");
    if (settingsBtn) settingsBtn.classList.toggle("d-none", !s.on);

    // синхронизируем модалку, если элементы есть
    const fontSel = document.getElementById("a11yFontSize");
    if (fontSel) fontSel.value = s.font;

    const c = (id, val) => {
      const el = document.getElementById(id);
      if (el) el.checked = !!val;
    };

    c("a11yContrast", s.contrast);
    c("a11yUnderlineLinks", s.underline);
    c("a11ySpacing", s.spacing);
    c("a11yReduceMotion", s.reduceMotion);
  }

  document.addEventListener("DOMContentLoaded", function () {
    let state = load();
    apply(state);

    const toggleBtn = document.getElementById("a11yToggle");
    if (toggleBtn) {
      toggleBtn.addEventListener("click", function () {
        state.on = !state.on;
        save(state);
        apply(state);
      });
    }

    const settingsBtn = document.getElementById("a11ySettingsBtn");
    if (settingsBtn) {
      settingsBtn.addEventListener("click", function () {
        const modalEl = document.getElementById("a11yModal");
        if (modalEl && window.bootstrap) {
          const m = bootstrap.Modal.getOrCreateInstance(modalEl);
          m.show();
        }
      });
    }

    const fontSel = document.getElementById("a11yFontSize");
    if (fontSel) {
      fontSel.addEventListener("change", function () {
        state.font = fontSel.value;
        save(state);
        apply(state);
      });
    }

    const bindSwitch = (id, key) => {
      const el = document.getElementById(id);
      if (!el) return;
      el.addEventListener("change", function () {
        state[key] = el.checked;
        save(state);
        apply(state);
      });
    };

    bindSwitch("a11yContrast", "contrast");
    bindSwitch("a11yUnderlineLinks", "underline");
    bindSwitch("a11ySpacing", "spacing");
    bindSwitch("a11yReduceMotion", "reduceMotion");

    const resetBtn = document.getElementById("a11yReset");
    if (resetBtn) {
      resetBtn.addEventListener("click", function () {
        state = { ...defaults };
        save(state);
        apply(state);
      });
    }
  });
})();
