document.addEventListener("DOMContentLoaded", () => {
  const search = document.querySelector("#skill-search");
  const status = document.querySelector("#status-filter");
  const security = document.querySelector("#security-filter");
  const category = document.querySelector("#category-filter");
  const source = document.querySelector("#source-filter");
  const results = document.querySelector("#results-count");
  const emptyState = document.querySelector("#empty-state");
  const cards = Array.from(document.querySelectorAll("[data-skill-card]"));
  const quickButtons = Array.from(document.querySelectorAll("[data-quick-filter]"));

  if (!cards.length) {
    return;
  }

  let activeQuick = "";

  const matchesQuickFilter = (card) => {
    if (!activeQuick) {
      return true;
    }

    if (activeQuick === "recommended") {
      return card.dataset.verdict === "recommended";
    }

    if (activeQuick === "low-install") {
      return card.dataset.install === "low";
    }

    if (activeQuick === "safe") {
      return ["A", "B"].includes(card.dataset.security);
    }

    if (activeQuick === "caution") {
      return card.dataset.verdict === "caution" || card.dataset.status !== "verified";
    }

    return true;
  };

  const applyFilters = () => {
    const query = (search?.value || "").trim().toLowerCase();
    const statusValue = status?.value || "";
    const securityValue = security?.value || "";
    const categoryValue = category?.value || "";
    const sourceValue = source?.value || "";

    let visible = 0;

    cards.forEach((card) => {
      const matchesSearch = !query || (card.dataset.search || "").includes(query);
      const matchesStatus = !statusValue || card.dataset.status === statusValue;
      const matchesSecurity = !securityValue || card.dataset.security === securityValue;
      const matchesCategory = !categoryValue || (card.dataset.category || "").split("|").includes(categoryValue);
      const matchesSource = !sourceValue || card.dataset.source === sourceValue;
      const matchesQuick = matchesQuickFilter(card);
      const isVisible = matchesSearch && matchesStatus && matchesSecurity && matchesCategory && matchesSource && matchesQuick;

      card.style.display = isVisible ? "flex" : "none";
      if (isVisible) {
        visible += 1;
      }
    });

    if (results) {
      results.textContent = `当前显示 ${visible} / ${cards.length} 个技能`;
    }

    if (emptyState) {
      emptyState.style.display = visible ? "none" : "block";
    }
  };

  quickButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const next = button.dataset.quickFilter || "";
      activeQuick = next === activeQuick || next === "reset" ? "" : next;
      quickButtons.forEach((item) => {
        item.classList.toggle("is-active", item.dataset.quickFilter === activeQuick);
      });
      applyFilters();
    });
  });

  document.querySelectorAll("[data-category-jump]").forEach((button) => {
    button.addEventListener("click", () => {
      const value = button.dataset.categoryJump || "";
      if (category) {
        category.value = value;
        applyFilters();
        document.querySelector("#skills")?.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  });

  [search, status, security, category, source].forEach((input) => {
    input?.addEventListener("input", applyFilters);
    input?.addEventListener("change", applyFilters);
  });

  applyFilters();
});
