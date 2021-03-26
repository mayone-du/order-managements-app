(() => {

  const $doc = document;


  // ログアウトのチェック
  const $logoutbutton = $doc.querySelector(".bl_logoutButton");
  if ($logoutbutton) {
    $logoutbutton.addEventListener("click", (e) => {
      if (confirm("ログアウトしますか？")) {
        return;
      } else {
        e.preventDefault();
      }
    })
  }


  // 実績削除のチェック
  const $deleteButton = $doc.querySelector(".bl_deleteButton");
  if ($deleteButton) {
    $deleteButton.addEventListener("click", (e) => {
      if (confirm("削除しますか？")) {
        return;
      } else {
        e.preventDefault();
      }
    })
  }


  // 値段を全て3桁で,区切り
  const $allPrice = $doc.querySelectorAll(".el_price");
  if ($allPrice) {
    for (let i = 0; i < $allPrice.length; i++) {
      const $price = $allPrice[i];
      const $priceText = $price.textContent;
      $price.textContent = parseFloat($priceText).toLocaleString();
    }
  }



  // 一覧のタブ
  const $tabAll = $doc.querySelector(".bl_tabButton_all");
  const $listAll = $doc.querySelector(".bl_listWrapper_all");
  const $tabDelivered = $doc.querySelector(".bl_tabButton_delivered");
  const $listDelivered = $doc.querySelector(".bl_listWrapper_delivered");
  const $tabUnDelivered = $doc.querySelector(".bl_tabButton_unDelivered");
  const $listUnDelivered = $doc.querySelector(".bl_listWrapper_unDelivered");


  if ($tabAll && $tabDelivered && $tabUnDelivered) {

    const otherInit = (otherTab, otherList) => {
      otherTab.classList.remove("st_isActive");
      otherList.classList.remove("st_isActive");
      otherList.classList.add("st_isDisabled");
    }
    
    const targetActive = (tab, list) => {
      list.classList.remove("st_isDisabled");
      list.classList.add("st_isActive");
      tab.classList.add("st_isActive");
    }

    $tabAll.addEventListener("click", () => {
      otherInit($tabDelivered, $listDelivered);
      otherInit($tabUnDelivered, $listUnDelivered);
      targetActive($tabAll, $listAll);
    })

    $tabDelivered.addEventListener("click", () => {
      otherInit($tabAll, $listAll);
      otherInit($tabUnDelivered, $listUnDelivered);
      targetActive($tabDelivered, $listDelivered);
    })

    $tabUnDelivered.addEventListener("click", () => {
      otherInit($tabAll, $listAll);
      otherInit($tabDelivered, $listDelivered);
      targetActive($tabUnDelivered, $listUnDelivered);
    })
    
  }


  

})();